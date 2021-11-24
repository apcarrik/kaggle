def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[12]<=2:
		# {"feature": "Age", "instances": 45, "metric_value": 0.8945, "depth": 2}
		if obj[4]>0:
			# {"feature": "Gender", "instances": 41, "metric_value": 0.839, "depth": 3}
			if obj[3]>0:
				# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 4}
				if obj[7]<=13:
					# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.9928, "depth": 5}
					if obj[10]<=2.0:
						# {"feature": "Passanger", "instances": 18, "metric_value": 1.0, "depth": 6}
						if obj[0]>0:
							# {"feature": "Coupon", "instances": 17, "metric_value": 0.9975, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Bar", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[8]<=3.0:
										# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[6]>0:
											# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[9]>2.0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											elif obj[9]<=2.0:
												return 'False'
											else: return 'False'
										elif obj[6]<=0:
											return 'True'
										else: return 'True'
									elif obj[8]>3.0:
										return 'False'
									else: return 'False'
								elif obj[1]>3:
									return 'True'
								else: return 'True'
							elif obj[2]>3:
								# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[9]<=1.0:
									return 'False'
								elif obj[9]>1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[10]>2.0:
						return 'True'
					else: return 'True'
				elif obj[7]>13:
					return 'True'
				else: return 'True'
			elif obj[3]<=0:
				# {"feature": "Education", "instances": 18, "metric_value": 0.5033, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.3228, "depth": 5}
					if obj[10]<=1.0:
						return 'True'
					elif obj[10]>1.0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'True'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]<=0:
			# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[3]<=0:
				return 'False'
			elif obj[3]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[12]>2:
		return 'False'
	else: return 'False'
