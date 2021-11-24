def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Driving_to", "instances": 41, "metric_value": 0.9996, "depth": 1}
	if obj[0]<=0:
		# {"feature": "Occupation", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[12]>7:
			# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[15]>1.0:
				# {"feature": "Income", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[13]<=4:
					return 'True'
				elif obj[13]>4:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=1:
						return 'False'
					elif obj[5]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[15]<=1.0:
				return 'False'
			else: return 'False'
		elif obj[12]<=7:
			return 'True'
		else: return 'True'
	elif obj[0]>0:
		# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.8113, "depth": 2}
		if obj[15]>1.0:
			# {"feature": "Income", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[13]>2:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[5]>0:
					return 'True'
				elif obj[5]<=0:
					return 'False'
				else: return 'False'
			elif obj[13]<=2:
				return 'False'
			else: return 'False'
		elif obj[15]<=1.0:
			return 'False'
		else: return 'False'
	else: return 'False'
