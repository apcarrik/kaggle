def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[15]>0.0:
		# {"feature": "Education", "instances": 24, "metric_value": 0.7383, "depth": 2}
		if obj[11]<=2:
			# {"feature": "Coupon", "instances": 19, "metric_value": 0.4855, "depth": 3}
			if obj[5]>0:
				# {"feature": "Income", "instances": 18, "metric_value": 0.3095, "depth": 4}
				if obj[13]>1:
					return 'True'
				elif obj[13]<=1:
					# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[9]<=0:
						return 'True'
					elif obj[9]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]<=0:
				return 'False'
			else: return 'False'
		elif obj[11]>2:
			# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[7]<=0:
				return 'False'
			elif obj[7]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[15]<=0.0:
		# {"feature": "Age", "instances": 10, "metric_value": 0.971, "depth": 2}
		if obj[8]>0:
			# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[7]>0:
				# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[13]<=4:
					return 'False'
				elif obj[13]>4:
					return 'True'
				else: return 'True'
			elif obj[7]<=0:
				return 'True'
			else: return 'True'
		elif obj[8]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
