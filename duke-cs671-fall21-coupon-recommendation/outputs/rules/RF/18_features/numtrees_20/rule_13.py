def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Age", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[6]>0:
		# {"feature": "Occupation", "instances": 46, "metric_value": 0.9781, "depth": 2}
		if obj[10]<=11:
			# {"feature": "Passanger", "instances": 37, "metric_value": 0.909, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Time", "instances": 27, "metric_value": 0.9751, "depth": 4}
				if obj[2]>0:
					# {"feature": "Income", "instances": 19, "metric_value": 0.998, "depth": 5}
					if obj[11]<=6:
						# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 6}
						if obj[9]<=2:
							# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.684, "depth": 7}
							if obj[7]<=1:
								return 'False'
							elif obj[7]>1:
								# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[4]>0:
									return 'False'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[9]>2:
							# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[3]<=2:
								return 'True'
							elif obj[3]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[11]>6:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					# {"feature": "Income", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[11]<=5:
						return 'True'
					elif obj[11]>5:
						# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]>0:
							return 'False'
						elif obj[5]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Time", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]>0:
						return 'True'
					elif obj[5]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[10]>11:
			# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[13]<=1.0:
				# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]>0:
						return 'False'
					elif obj[5]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[13]>1.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[6]<=0:
		return 'True'
	else: return 'True'
