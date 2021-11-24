def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[9]<=2.0:
		# {"feature": "Bar", "instances": 49, "metric_value": 0.9973, "depth": 2}
		if obj[7]<=2.0:
			# {"feature": "Time", "instances": 46, "metric_value": 1.0, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 4}
				if obj[6]>2:
					# {"feature": "Passanger", "instances": 27, "metric_value": 0.999, "depth": 5}
					if obj[0]>0:
						# {"feature": "Coupon", "instances": 25, "metric_value": 0.9988, "depth": 6}
						if obj[2]>0:
							# {"feature": "Age", "instances": 22, "metric_value": 0.994, "depth": 7}
							if obj[4]<=5:
								# {"feature": "Gender", "instances": 20, "metric_value": 1.0, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Direction_same", "instances": 11, "metric_value": 0.9457, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 10}
										if obj[5]<=2:
											# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.9544, "depth": 12}
												if obj[8]<=2.0:
													return 'False'
												elif obj[8]>2.0:
													return 'False'
												else: return 'False'
											elif obj[11]>2:
												return 'False'
											else: return 'False'
										elif obj[5]>2:
											return 'False'
										else: return 'False'
									elif obj[10]>0:
										return 'True'
									else: return 'True'
								elif obj[3]>0:
									# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 9}
									if obj[11]<=2:
										# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 10}
										if obj[5]<=2:
											# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[8]<=0.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[8]>0.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>2:
											return 'True'
										else: return 'True'
									elif obj[11]>2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]>5:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[6]<=2:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[0]>1:
						return 'False'
					elif obj[0]<=1:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=2:
							return 'False'
						elif obj[4]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[6]>4:
					# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[4]<=4:
						# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[2]>3:
							# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=2:
								# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8]<=1.0:
									return 'False'
								elif obj[8]>1.0:
									return 'True'
								else: return 'True'
							elif obj[5]>2:
								return 'True'
							else: return 'True'
						elif obj[2]<=3:
							return 'False'
						else: return 'False'
					elif obj[4]>4:
						return 'True'
					else: return 'True'
				elif obj[6]<=4:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[7]>2.0:
			return 'True'
		else: return 'True'
	elif obj[9]>2.0:
		return 'False'
	else: return 'False'
