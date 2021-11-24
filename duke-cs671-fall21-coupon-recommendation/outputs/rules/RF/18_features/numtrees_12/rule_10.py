def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9465, "depth": 1}
	if obj[3]>1:
		# {"feature": "Income", "instances": 61, "metric_value": 0.8537, "depth": 2}
		if obj[11]<=7:
			# {"feature": "Age", "instances": 54, "metric_value": 0.8987, "depth": 3}
			if obj[6]<=5:
				# {"feature": "Time", "instances": 46, "metric_value": 0.8281, "depth": 4}
				if obj[2]>0:
					# {"feature": "Occupation", "instances": 36, "metric_value": 0.7107, "depth": 5}
					if obj[10]<=6:
						# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.8813, "depth": 6}
						if obj[13]<=2.0:
							# {"feature": "Weather", "instances": 19, "metric_value": 0.8315, "depth": 7}
							if obj[1]<=0:
								# {"feature": "Restaurantlessthan20", "instances": 14, "metric_value": 0.9403, "depth": 8}
								if obj[14]<=2.0:
									# {"feature": "Children", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[8]>0:
										# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[17]>1:
											return 'True'
										elif obj[17]<=1:
											return 'False'
										else: return 'False'
									elif obj[8]<=0:
										# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[9]<=2:
											return 'False'
										elif obj[9]>2:
											# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[0]>1:
												return 'False'
											elif obj[0]<=1:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								elif obj[14]>2.0:
									return 'True'
								else: return 'True'
							elif obj[1]>0:
								return 'True'
							else: return 'True'
						elif obj[13]>2.0:
							return 'False'
						else: return 'False'
					elif obj[10]>6:
						# {"feature": "Distance", "instances": 16, "metric_value": 0.3373, "depth": 6}
						if obj[17]<=2:
							return 'True'
						elif obj[17]>2:
							# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[7]>0:
								return 'False'
							elif obj[7]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[2]<=0:
					# {"feature": "Bar", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[12]>0.0:
						# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[10]<=6:
							return 'True'
						elif obj[10]>6:
							# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]<=0:
								return 'False'
							elif obj[7]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[12]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]>5:
				# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[9]>2:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]<=2:
						return 'True'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				elif obj[9]<=2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[11]>7:
			return 'True'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Bar", "instances": 24, "metric_value": 0.9799, "depth": 2}
		if obj[12]<=1.0:
			# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.7642, "depth": 3}
			if obj[13]>0.0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[10]<=12:
					return 'False'
				elif obj[10]>12:
					return 'True'
				else: return 'True'
			elif obj[13]<=0.0:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[12]>1.0:
			return 'True'
		else: return 'True'
	else: return 'False'
