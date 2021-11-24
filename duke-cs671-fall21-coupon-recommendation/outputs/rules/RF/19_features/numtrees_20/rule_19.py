def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[4]>1:
		# {"feature": "Passanger", "instances": 34, "metric_value": 0.99, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 29, "metric_value": 0.9991, "depth": 3}
			if obj[10]<=0:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[11]<=12:
					# {"feature": "Income", "instances": 13, "metric_value": 0.7793, "depth": 5}
					if obj[12]<=2:
						# {"feature": "Children", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[9]<=0:
							# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[2]<=55:
								return 'True'
							elif obj[2]>55:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]>1:
									return 'False'
								elif obj[3]<=1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[9]>0:
							return 'False'
						else: return 'False'
					elif obj[12]>2:
						return 'True'
					else: return 'True'
				elif obj[11]>12:
					return 'False'
				else: return 'False'
			elif obj[10]>0:
				# {"feature": "Occupation", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[11]<=11:
					# {"feature": "Time", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[3]<=1:
						return 'False'
					elif obj[3]>1:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[7]>0:
							return 'True'
						elif obj[7]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[11]>11:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	elif obj[4]<=1:
		# {"feature": "Bar", "instances": 17, "metric_value": 0.6723, "depth": 2}
		if obj[13]<=1.0:
			return 'False'
		elif obj[13]>1.0:
			# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[11]<=7:
				return 'True'
			elif obj[11]>7:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
