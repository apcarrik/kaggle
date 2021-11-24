def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Income", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[11]>5:
			# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[13]>0.0:
				return 'False'
			elif obj[13]<=0.0:
				# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[11]<=5:
			# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[3]>0:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[10]>1:
					return 'True'
				elif obj[10]<=1:
					return 'False'
				else: return 'False'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Coupon", "instances": 16, "metric_value": 0.8113, "depth": 2}
		if obj[3]>2:
			# {"feature": "Restaurantlessthan20", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[14]>1.0:
				# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[9]>0:
					return 'True'
				elif obj[9]<=0:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[14]<=1.0:
				return 'False'
			else: return 'False'
		elif obj[3]<=2:
			return 'True'
		else: return 'True'
	else: return 'True'
