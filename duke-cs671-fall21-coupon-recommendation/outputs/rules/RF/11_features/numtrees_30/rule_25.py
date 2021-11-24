def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[10]<=2:
		# {"feature": "Occupation", "instances": 31, "metric_value": 0.9072, "depth": 2}
		if obj[5]<=18:
			# {"feature": "Age", "instances": 29, "metric_value": 0.8498, "depth": 3}
			if obj[3]>0:
				# {"feature": "Education", "instances": 24, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=3:
					# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9587, "depth": 5}
					if obj[8]>-1.0:
						# {"feature": "Direction_same", "instances": 20, "metric_value": 0.9341, "depth": 6}
						if obj[9]<=0:
							# {"feature": "Coupon", "instances": 19, "metric_value": 0.8997, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Bar", "instances": 10, "metric_value": 0.7219, "depth": 8}
								if obj[6]<=1.0:
									# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[0]>0:
										# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[7]>1.0:
											# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[1]<=2:
												return 'True'
											elif obj[1]>2:
												return 'True'
											else: return 'True'
										elif obj[7]<=1.0:
											return 'True'
										else: return 'True'
									elif obj[0]<=0:
										return 'False'
									else: return 'False'
								elif obj[6]>1.0:
									return 'True'
								else: return 'True'
							elif obj[2]>3:
								# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[7]>1.0:
									# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[6]>0.0:
										return 'True'
									elif obj[6]<=0.0:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0]>1:
											return 'False'
										elif obj[0]<=1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[7]<=1.0:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1]<=0:
											# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6]<=0.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[9]>0:
							return 'False'
						else: return 'False'
					elif obj[8]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[4]>3:
					return 'True'
				else: return 'True'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		elif obj[5]>18:
			return 'False'
		else: return 'False'
	elif obj[10]>2:
		return 'False'
	else: return 'False'
