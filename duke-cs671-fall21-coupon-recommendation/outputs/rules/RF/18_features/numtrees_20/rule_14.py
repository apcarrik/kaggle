def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[10]>2:
		# {"feature": "Weather", "instances": 38, "metric_value": 0.868, "depth": 2}
		if obj[1]<=0:
			# {"feature": "Income", "instances": 31, "metric_value": 0.7088, "depth": 3}
			if obj[11]>1:
				# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.8631, "depth": 4}
				if obj[13]>1.0:
					# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[3]>1:
						return 'True'
					elif obj[3]<=1:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[13]<=1.0:
					# {"feature": "Time", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[17]>1:
							return 'True'
						elif obj[17]<=1:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]>3:
								return 'False'
							elif obj[3]<=3:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[11]<=1:
				return 'True'
			else: return 'True'
		elif obj[1]>0:
			# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[12]<=0.0:
				return 'False'
			elif obj[12]>0.0:
				# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[8]<=0:
					return 'True'
				elif obj[8]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[10]<=2:
		# {"feature": "Time", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[2]<=1:
			return 'False'
		elif obj[2]>1:
			# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
