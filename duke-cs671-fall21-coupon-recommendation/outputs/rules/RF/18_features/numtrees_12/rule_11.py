def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[3]>0:
		# {"feature": "Occupation", "instances": 68, "metric_value": 0.9367, "depth": 2}
		if obj[10]<=13:
			# {"feature": "Restaurantlessthan20", "instances": 65, "metric_value": 0.9077, "depth": 3}
			if obj[14]>0.0:
				# {"feature": "Weather", "instances": 63, "metric_value": 0.8832, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Distance", "instances": 53, "metric_value": 0.9245, "depth": 5}
					if obj[17]>1:
						# {"feature": "Income", "instances": 27, "metric_value": 0.9911, "depth": 6}
						if obj[11]<=6:
							# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.994, "depth": 7}
							if obj[13]>0.0:
								# {"feature": "Education", "instances": 17, "metric_value": 0.9367, "depth": 8}
								if obj[9]<=2:
									# {"feature": "Age", "instances": 14, "metric_value": 0.9852, "depth": 9}
									if obj[6]<=2:
										# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[15]<=1.0:
											return 'False'
										elif obj[15]>1.0:
											# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[8]>0:
												return 'True'
											elif obj[8]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[6]>2:
										# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[2]>0:
											# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[0]>1:
												# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7]<=0:
													return 'True'
												elif obj[7]>0:
													return 'False'
												else: return 'False'
											elif obj[0]<=1:
												return 'False'
											else: return 'False'
										elif obj[2]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[9]>2:
									return 'False'
								else: return 'False'
							elif obj[13]<=0.0:
								# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[6]>1:
									return 'True'
								elif obj[6]<=1:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[11]>6:
							return 'True'
						else: return 'True'
					elif obj[17]<=1:
						# {"feature": "Age", "instances": 26, "metric_value": 0.7793, "depth": 6}
						if obj[6]>0:
							# {"feature": "Bar", "instances": 20, "metric_value": 0.8813, "depth": 7}
							if obj[12]<=1.0:
								# {"feature": "Coupon_validity", "instances": 16, "metric_value": 0.6962, "depth": 8}
								if obj[4]<=0:
									# {"feature": "Income", "instances": 9, "metric_value": 0.9183, "depth": 9}
									if obj[11]>2:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[5]>0:
											return 'True'
										elif obj[5]<=0:
											return 'False'
										else: return 'False'
									elif obj[11]<=2:
										# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[2]<=0:
											return 'False'
										elif obj[2]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[4]>0:
									return 'True'
								else: return 'True'
							elif obj[12]>1.0:
								# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[2]<=1:
									return 'False'
								elif obj[2]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[6]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]>0:
					# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[13]<=3.0:
						return 'True'
					elif obj[13]>3.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[14]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[10]>13:
			return 'False'
		else: return 'False'
	elif obj[3]<=0:
		# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.6723, "depth": 2}
		if obj[13]<=2.0:
			return 'False'
		elif obj[13]>2.0:
			# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[2]>0:
				# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[15]>-1.0:
					return 'True'
				elif obj[15]<=-1.0:
					return 'False'
				else: return 'False'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
