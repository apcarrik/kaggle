def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[12]<=10:
		# {"feature": "Temperature", "instances": 28, "metric_value": 0.9852, "depth": 2}
		if obj[3]<=55:
			# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[17]<=1.0:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[5]>0:
					# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[7]<=0:
						return 'True'
					elif obj[7]>0:
						# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'True'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]<=0:
					# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[13]>1:
						return 'False'
					elif obj[13]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[17]>1.0:
				return 'False'
			else: return 'False'
		elif obj[3]>55:
			# {"feature": "Driving_to", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[12]>10:
		return 'False'
	else: return 'False'
