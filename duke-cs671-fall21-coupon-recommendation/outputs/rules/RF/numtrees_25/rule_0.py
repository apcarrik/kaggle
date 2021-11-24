def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Bar", "instances": 41, "metric_value": 0.8722, "depth": 1}
	if obj[14]>0.0:
		# {"feature": "Restaurantlessthan20", "instances": 27, "metric_value": 0.6052, "depth": 2}
		if obj[17]>1.0:
			# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.258, "depth": 3}
			if obj[18]>0.0:
				return 'True'
			elif obj[18]<=0.0:
				# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[8]<=1:
					return 'True'
				elif obj[8]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[17]<=1.0:
			# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[5]>0:
				return 'False'
			elif obj[5]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[14]<=0.0:
		# {"feature": "Passanger", "instances": 14, "metric_value": 0.9852, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Temperature", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[3]<=55:
				return 'False'
			elif obj[3]>55:
				# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
