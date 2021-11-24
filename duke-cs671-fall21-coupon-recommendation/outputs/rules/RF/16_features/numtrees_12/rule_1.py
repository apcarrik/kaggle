def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[9]<=12:
		# {"feature": "Distance", "instances": 74, "metric_value": 0.9916, "depth": 2}
		if obj[15]>1:
			# {"feature": "Education", "instances": 39, "metric_value": 0.8905, "depth": 3}
			if obj[8]<=3:
				# {"feature": "Bar", "instances": 36, "metric_value": 0.8113, "depth": 4}
				if obj[11]>0.0:
					# {"feature": "Income", "instances": 23, "metric_value": 0.9656, "depth": 5}
					if obj[10]>1:
						# {"feature": "Direction_same", "instances": 21, "metric_value": 0.9183, "depth": 6}
						if obj[14]<=0:
							# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.8813, "depth": 7}
							if obj[13]>0.0:
								# {"feature": "Age", "instances": 16, "metric_value": 0.9544, "depth": 8}
								if obj[6]<=3:
									# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[2]<=2:
										# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[1]<=0:
											# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3]<=2:
												return 'True'
											elif obj[3]>2:
												return 'False'
											else: return 'False'
										elif obj[1]>0:
											return 'False'
										else: return 'False'
									elif obj[2]>2:
										return 'False'
									else: return 'False'
								elif obj[6]>3:
									# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[3]>1:
											# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[2]<=0:
												return 'True'
											elif obj[2]>0:
												return 'False'
											else: return 'False'
										elif obj[3]<=1:
											return 'False'
										else: return 'False'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[13]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[14]>0:
							return 'True'
						else: return 'True'
					elif obj[10]<=1:
						return 'True'
					else: return 'True'
				elif obj[11]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[8]>3:
				return 'True'
			else: return 'True'
		elif obj[15]<=1:
			# {"feature": "Weather", "instances": 35, "metric_value": 0.971, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Income", "instances": 33, "metric_value": 0.9457, "depth": 4}
				if obj[10]<=5:
					# {"feature": "Passanger", "instances": 23, "metric_value": 0.9986, "depth": 5}
					if obj[0]>0:
						# {"feature": "Children", "instances": 21, "metric_value": 0.9984, "depth": 6}
						if obj[7]<=0:
							# {"feature": "Bar", "instances": 12, "metric_value": 0.9183, "depth": 7}
							if obj[11]<=1.0:
								# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[8]>2:
									# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[6]>1:
										return 'False'
									elif obj[6]<=1:
										# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[2]>0:
											return 'False'
										elif obj[2]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]<=2:
									# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[2]>0:
										# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5]<=0:
											return 'False'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									elif obj[2]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[11]>1.0:
								return 'False'
							else: return 'False'
						elif obj[7]>0:
							# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[3]>3:
								# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[11]<=0.0:
									return 'False'
								elif obj[11]>0.0:
									return 'True'
								else: return 'True'
							elif obj[3]<=3:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[10]>5:
					# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[6]<=5:
						return 'True'
					elif obj[6]>5:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[9]>12:
		# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[12]>0.0:
			return 'True'
		elif obj[12]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'True'
