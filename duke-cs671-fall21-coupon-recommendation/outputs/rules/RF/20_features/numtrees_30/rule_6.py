def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.8338, "depth": 1}
	if obj[5]>1:
		# {"feature": "Distance", "instances": 28, "metric_value": 0.5917, "depth": 2}
		if obj[19]<=2:
			# {"feature": "Maritalstatus", "instances": 25, "metric_value": 0.4022, "depth": 3}
			if obj[9]<=2:
				# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.258, "depth": 4}
				if obj[15]>0.0:
					return 'True'
				elif obj[15]<=0.0:
					# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]>0:
						return 'True'
					elif obj[6]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[9]>2:
				# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=0:
					return 'True'
				elif obj[0]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[19]>2:
			# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[13]>2:
				return 'False'
			elif obj[13]<=2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[5]<=1:
		# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[8]<=2:
			return 'False'
		elif obj[8]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
