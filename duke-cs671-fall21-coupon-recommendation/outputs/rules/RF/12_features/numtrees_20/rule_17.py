def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[8]>0.0:
		# {"feature": "Restaurant20to50", "instances": 47, "metric_value": 0.9252, "depth": 2}
		if obj[9]>0.0:
			# {"feature": "Coupon", "instances": 45, "metric_value": 0.8945, "depth": 3}
			if obj[2]>1:
				# {"feature": "Education", "instances": 40, "metric_value": 0.9341, "depth": 4}
				if obj[5]<=3:
					# {"feature": "Passanger", "instances": 37, "metric_value": 0.9569, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Occupation", "instances": 21, "metric_value": 0.9984, "depth": 6}
						if obj[6]<=10:
							# {"feature": "Bar", "instances": 18, "metric_value": 0.9641, "depth": 7}
							if obj[7]<=1.0:
								# {"feature": "Distance", "instances": 14, "metric_value": 1.0, "depth": 8}
								if obj[11]<=2:
									# {"feature": "Time", "instances": 12, "metric_value": 0.9799, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[4]<=5:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if obj[3]<=0:
												return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>5:
											return 'False'
										else: return 'False'
									elif obj[1]>2:
										# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[4]<=6:
											return 'False'
										elif obj[4]>6:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[11]>2:
									return 'False'
								else: return 'False'
							elif obj[7]>1.0:
								return 'True'
							else: return 'True'
						elif obj[6]>10:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						# {"feature": "Distance", "instances": 16, "metric_value": 0.8113, "depth": 6}
						if obj[11]>1:
							# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[4]>1:
								return 'True'
							elif obj[4]<=1:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]>0:
										return 'True'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								elif obj[1]>2:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[11]<=1:
							# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[1]>2:
								# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[6]<=9:
									return 'True'
								elif obj[6]>9:
									# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4]>1:
										return 'False'
									elif obj[4]<=1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]<=2:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[5]>3:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				return 'True'
			else: return 'True'
		elif obj[9]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[8]<=0.0:
		return 'False'
	else: return 'False'
