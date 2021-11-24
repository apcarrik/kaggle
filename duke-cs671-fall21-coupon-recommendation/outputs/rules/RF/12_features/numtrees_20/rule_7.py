def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[6]>1:
		# {"feature": "Education", "instances": 45, "metric_value": 0.971, "depth": 2}
		if obj[5]<=1:
			# {"feature": "Passanger", "instances": 23, "metric_value": 0.7554, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Age", "instances": 14, "metric_value": 0.9403, "depth": 4}
				if obj[4]<=5:
					# {"feature": "Coffeehouse", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[8]>0.0:
						# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[7]<=1.0:
							# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[1]<=0:
								return 'True'
							elif obj[1]>0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[10]<=0:
									return 'True'
								elif obj[10]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[7]>1.0:
							return 'False'
						else: return 'False'
					elif obj[8]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[4]>5:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[5]>1:
			# {"feature": "Age", "instances": 22, "metric_value": 0.976, "depth": 3}
			if obj[4]>0:
				# {"feature": "Time", "instances": 20, "metric_value": 0.9341, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Coupon", "instances": 17, "metric_value": 0.9774, "depth": 5}
					if obj[2]>0:
						# {"feature": "Bar", "instances": 14, "metric_value": 1.0, "depth": 6}
						if obj[7]>-1.0:
							# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 7}
							if obj[9]>1.0:
								# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[8]<=2.0:
									return 'False'
								elif obj[8]>2.0:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[11]>1:
										return 'True'
									elif obj[11]<=1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[9]<=1.0:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[10]<=0:
									# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[0]>1:
										# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=0.0:
											# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]<=1:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]>0.0:
											return 'True'
										else: return 'True'
									elif obj[0]<=1:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=1.0:
											return 'True'
										elif obj[8]>1.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[10]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]<=-1.0:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[6]<=1:
		return 'True'
	else: return 'True'
