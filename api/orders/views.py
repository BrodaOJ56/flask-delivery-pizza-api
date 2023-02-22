from flask_restx import Namespace, Resource, fields
from ..models.orders import Order
from ..models.users import User
from ..utils import db
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity

order_namespace = Namespace('orders', description='Namespace for Orders')

order_model = order_namespace.model(
    'Order', {
        'id': fields.Integer(description='Order ID'),
        'flavour': fields.String(description='Pizza Flavour', required=True),
         'quantity': fields.Integer(description='Number of Pizzas'),
        'size': fields.String(description='Pizza Size', required=True,
            enum = ['SMALL', 'MEDIUM', 'LARGE', 'EXTRA_LARGE']
        ),
        'order_status': fields.String(description='Current Order Status', required=True,
            enum = ['PENDING', 'IN_TRANSIT', 'DELIVERED']
        )
    }
)

order_status_model = order_namespace.model(
    'OrderStatus', {
        'order_status': fields.String(description='Current Order Status', required=True,
            enum = ['PENDING', 'IN_TRANSIT', 'DELIVERED'])
    }
)

@order_namespace.route('/orders')
class OrderGetCreate(Resource):

    @order_namespace.marshal_with(order_model)
    @order_namespace.doc(
        description="Retrieve all orders"
    )
    @jwt_required()
    def get(self):
        """
            Get All Orders
        """
        orders = Order.query.all()

        return orders, HTTPStatus.OK

    @order_namespace.expect(order_model)
    @order_namespace.marshal_with(order_model)
    @order_namespace.doc(
        description="Place an order")
    @jwt_required()
    def post(self):
        """
            Place an Order
        """

        username = get_jwt_identity()

        current_user = User.query.filter_by(username=username).first()

        data = order_namespace.payload

        new_order = Order(
            size = data['size'],
            quantity = data['quantity'],
            flavour = data['flavour']
        )

        new_order.user = current_user

        new_order.save()

        return new_order, HTTPStatus.CREATED


@order_namespace.route('/order/<int:order_id>')
class GetUpdateDelete(Resource):

    @order_namespace.marshal_with(order_model)
    @order_namespace.doc(
        description="Retrieve an order by its ID" ,
        params={
            "order_id":"An ID for a given order"
            }
            )
    @jwt_required()
    def get(self, order_id):
        """
            Retrieve an Order by ID
        """        
        order = Order.get_by_id(order_id)

        return order, HTTPStatus.OK

    @order_namespace.expect(order_model)
    @order_namespace.marshal_with(order_model)
    @order_namespace.doc(
        description="Update an order given an order ID" ,
        params={
            "order_id":"An ID for a given order"
            }
            )
    @jwt_required()
    def put(self, order_id):
        """
            Update an Order by ID
        """
        order_to_update = Order.get_by_id(order_id)

        data = order_namespace.payload

        order_to_update.flavour = data["flavour"]
        order_to_update.quantity = data["quantity"]
        order_to_update.size = data["size"]

        order_to_update.update()

        return order_to_update, HTTPStatus.OK
    @order_namespace.doc(
        description="Delete an orders given an order ID " ,
        params={
            "order_id":"An ID for a given order"
            }
            )    

    @jwt_required()
    def delete(self, order_id):
        """
            Delete an Order by ID
        """
        order_to_delete = Order.get_by_id(order_id)

        order_to_delete.delete()

        return {"message": "Order Deleted Successfully"}, HTTPStatus.OK

@order_namespace.route('/user/<int:user_id>/order/<int:order_id>')
class GetSpecificOrderByUser(Resource):

    @order_namespace.marshal_with(order_model)
    @order_namespace.doc(
        description="Get a user's specific order" ,
        params={
            "order_id":"An ID for a given order" ,
            "user_id":"A user's ID"
            }
            )
    @jwt_required()    
    def get(self, user_id, order_id):
        """
            Get a User's Specific Order
        """
        user = User.get_by_id(user_id)

        order = Order.query.filter_by(id=order_id).filter_by(user=user).first()

        return order, HTTPStatus.OK

@order_namespace.route('/user/<int:user_id>/orders')
class UserOrders(Resource):

    @order_namespace.marshal_list_with(order_model)
    @order_namespace.doc(
        description="Get Orders of a user given the user ID" ,
        params={
            "user_id":"An ID for a given user"
            }
            )
    @jwt_required()
    def get(self, user_id):
        """
            Get All Orders by a User
        """
        user = User.get_by_id(user_id)

        orders = user.orders

        return orders, HTTPStatus.OK

@order_namespace.route('/order/status/<int:order_id>')
class UpdateOrderStatus(Resource):
    @order_namespace.doc(
        description="Update an order's status given the order ID" ,
        params={
            "order_id":"An ID for a given order"
            }
            )
    @order_namespace.expect(order_status_model)
    @order_namespace.marshal_with(order_model)
    
    @jwt_required()
    def patch(self, order_id):
        """
            Update an Order's Status
        """
        data = order_namespace.payload

        order_to_update = Order.get_by_id(order_id)

        order_to_update.order_status = data["order_status"]

        db.session.commit()

        return order_to_update, HTTPStatus.OK