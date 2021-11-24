def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9555, "depth": 1}
	if obj[11]<=2:
		# {"feature": "Education", "instances": 74, "metric_value": 0.909, "depth": 2}
		if obj[5]>1:
			# {"feature": "Occupation", "instances": 38, "metric_value": 0.9819, "depth": 3}
			if obj[6]<=20:
				# {"feature": "Time", "instances": 36, "metric_value": 0.9641, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.9968, "depth": 5}
					if obj[9]>-1.0:
						# {"feature": "Coupon", "instances": 29, "metric_value": 0.9923, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.9495, "depth": 7}
							if obj[8]<=2.0:
								# {"feature": "Age", "instances": 13, "metric_value": 0.7793, "depth": 8}
								if obj[4]<=4:
									# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 9}
									if obj[0]>0:
										return 'True'
									elif obj[0]<=0:
										# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7]<=1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>4:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]<=1:
										return 'False'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[8]>2.0:
								# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[4]>0:
									# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[3]>0:
										# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7]<=0.0:
												return 'True'
											elif obj[7]>0.0:
												return 'False'
											else: return 'False'
										elif obj[0]>1:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								elif obj[4]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[2]>3:
							# {"feature": "Direction_same", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[10]<=0:
								# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[8]<=3.0:
										return 'True'
									elif obj[8]>3.0:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0]>1:
											return 'True'
										elif obj[0]<=1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[7]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[10]>0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[9]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[6]>20:
				return 'False'
			else: return 'False'
		elif obj[5]<=1:
			# {"feature": "Coffeehouse", "instances": 36, "metric_value": 0.7642, "depth": 3}
			if obj[8]<=2.0:
				# {"feature": "Coupon", "instances": 28, "metric_value": 0.8631, "depth": 4}
				if obj[2]>0:
					# {"feature": "Passanger", "instances": 26, "metric_value": 0.7793, "depth": 5}
					if obj[0]>1:
						# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.3912, "depth": 6}
						if obj[9]<=1.0:
							return 'True'
						elif obj[9]>1.0:
							# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]>5:
								return 'True'
							elif obj[4]<=5:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[0]<=1:
						# {"feature": "Occupation", "instances": 13, "metric_value": 0.9612, "depth": 6}
						if obj[6]>3:
							# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[4]>2:
								# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[1]<=3:
									return 'True'
								elif obj[1]>3:
									return 'False'
								else: return 'False'
							elif obj[4]<=2:
								return 'False'
							else: return 'False'
						elif obj[6]<=3:
							# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[1]>0:
								return 'True'
							elif obj[1]<=0:
								# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]>0:
									return 'False'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[8]>2.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[11]>2:
		# {"feature": "Coupon", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[2]<=2:
			return 'False'
		elif obj[2]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
