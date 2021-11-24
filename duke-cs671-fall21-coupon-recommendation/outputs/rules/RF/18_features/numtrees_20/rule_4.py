def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Weather", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[1]<=0:
		# {"feature": "Restaurant20to50", "instances": 44, "metric_value": 0.9624, "depth": 2}
		if obj[15]<=1.0:
			# {"feature": "Passanger", "instances": 28, "metric_value": 0.8113, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Income", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[11]<=6:
					# {"feature": "Age", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[6]>2:
						# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[2]<=1:
							return 'True'
						elif obj[2]>1:
							return 'False'
						else: return 'False'
					elif obj[6]<=2:
						return 'False'
					else: return 'False'
				elif obj[11]>6:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Bar", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[12]<=2.0:
					return 'True'
				elif obj[12]>2.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[15]>1.0:
			# {"feature": "Coupon_validity", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[4]>0:
				# {"feature": "Gender", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[5]>0:
					return 'False'
				elif obj[5]<=0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]<=0:
				# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[7]>0:
					return 'True'
				elif obj[7]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[1]>0:
		return 'False'
	else: return 'False'
