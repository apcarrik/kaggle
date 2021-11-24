def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[10]<=9:
		# {"feature": "Bar", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[12]>0.0:
			return 'True'
		elif obj[12]<=0.0:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[0]>2:
				# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[6]>4:
					# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[11]>0:
						return 'False'
					elif obj[11]<=0:
						return 'True'
					else: return 'True'
				elif obj[6]<=4:
					return 'True'
				else: return 'True'
			elif obj[0]<=2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[10]>9:
		# {"feature": "Income", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[11]>1:
			# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[13]<=2.0:
				return 'False'
			elif obj[13]>2.0:
				# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[5]<=0:
					return 'False'
				elif obj[5]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[11]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
