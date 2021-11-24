def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Direction_same", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[16]<=0:
		# {"feature": "Coupon", "instances": 44, "metric_value": 0.994, "depth": 2}
		if obj[3]<=3:
			# {"feature": "Occupation", "instances": 32, "metric_value": 0.9544, "depth": 3}
			if obj[10]<=16:
				# {"feature": "Time", "instances": 28, "metric_value": 0.9852, "depth": 4}
				if obj[2]>0:
					# {"feature": "Income", "instances": 25, "metric_value": 0.9427, "depth": 5}
					if obj[11]<=6:
						# {"feature": "Bar", "instances": 21, "metric_value": 0.9852, "depth": 6}
						if obj[12]<=2.0:
							# {"feature": "Restaurantlessthan20", "instances": 17, "metric_value": 0.9975, "depth": 7}
							if obj[14]<=2.0:
								# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9852, "depth": 8}
								if obj[15]<=1.0:
									# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[5]>0:
										# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[6]<=3:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[0]<=2:
												# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[17]>1:
													return 'True'
												elif obj[17]<=1:
													return 'False'
												else: return 'False'
											elif obj[0]>2:
												return 'False'
											else: return 'False'
										elif obj[6]>3:
											return 'True'
										else: return 'True'
									elif obj[5]<=0:
										return 'False'
									else: return 'False'
								elif obj[15]>1.0:
									# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[17]>1:
										return 'True'
									elif obj[17]<=1:
										# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1]<=0:
											return 'True'
										elif obj[1]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[14]>2.0:
								return 'False'
							else: return 'False'
						elif obj[12]>2.0:
							return 'True'
						else: return 'True'
					elif obj[11]>6:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[10]>16:
				return 'True'
			else: return 'True'
		elif obj[3]>3:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[10]<=7:
				# {"feature": "Income", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[11]>4:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[11]<=4:
					return 'True'
				else: return 'True'
			elif obj[10]>7:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[16]>0:
		return 'True'
	else: return 'True'
