def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Bar", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[9]<=2.0:
		# {"feature": "Occupation", "instances": 46, "metric_value": 0.9986, "depth": 2}
		if obj[7]<=19:
			# {"feature": "Education", "instances": 43, "metric_value": 0.9996, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.9852, "depth": 4}
				if obj[11]<=2.0:
					# {"feature": "Coupon", "instances": 32, "metric_value": 0.9972, "depth": 5}
					if obj[2]>1:
						# {"feature": "Time", "instances": 20, "metric_value": 0.9341, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Income", "instances": 14, "metric_value": 1.0, "depth": 7}
							if obj[8]>3:
								# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 8}
								if obj[10]>0.0:
									# {"feature": "Gender", "instances": 10, "metric_value": 0.8813, "depth": 9}
									if obj[3]>0:
										# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[13]>1:
											# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[4]>1:
												return 'True'
											elif obj[4]<=1:
												# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[5]<=0:
														# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=0:
															return 'True'
														else: return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[13]<=1:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								elif obj[10]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[8]<=3:
								return 'False'
							else: return 'False'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						# {"feature": "Income", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[8]>4:
							return 'False'
						elif obj[8]<=4:
							# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=1:
								return 'True'
							elif obj[4]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[11]>2.0:
					return 'True'
				else: return 'True'
			elif obj[6]>2:
				# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[4]<=6:
					return 'False'
				elif obj[4]>6:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[7]>19:
			return 'True'
		else: return 'True'
	elif obj[9]>2.0:
		return 'True'
	else: return 'True'
