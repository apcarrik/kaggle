def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[13]<=3.0:
		# {"feature": "Time", "instances": 48, "metric_value": 0.995, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Restaurant20to50", "instances": 36, "metric_value": 0.9641, "depth": 3}
			if obj[14]>0.0:
				# {"feature": "Occupation", "instances": 32, "metric_value": 0.9887, "depth": 4}
				if obj[10]>2:
					# {"feature": "Age", "instances": 25, "metric_value": 0.9988, "depth": 5}
					if obj[6]<=6:
						# {"feature": "Maritalstatus", "instances": 24, "metric_value": 0.995, "depth": 6}
						if obj[7]<=1:
							# {"feature": "Passanger", "instances": 22, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Children", "instances": 15, "metric_value": 0.971, "depth": 8}
								if obj[8]>0:
									# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[16]>1:
										# {"feature": "Weather", "instances": 8, "metric_value": 0.5436, "depth": 10}
										if obj[1]<=1:
											return 'False'
										elif obj[1]>1:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[5]>0:
												return 'False'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[16]<=1:
										return 'True'
									else: return 'True'
								elif obj[8]<=0:
									# {"feature": "Coupon_validity", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[4]<=0:
										return 'True'
									elif obj[4]>0:
										# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[9]>1:
											return 'False'
										elif obj[9]<=1:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[0]>1:
								# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[12]>0.0:
									return 'True'
								elif obj[12]<=0.0:
									# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]>3:
										return 'False'
									elif obj[3]<=3:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[7]>1:
							return 'False'
						else: return 'False'
					elif obj[6]>6:
						return 'True'
					else: return 'True'
				elif obj[10]<=2:
					# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[6]>0:
						return 'True'
					elif obj[6]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[14]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[2]>3:
			# {"feature": "Age", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[6]<=3:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[0]>1:
					# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]<=1:
						return 'False'
					elif obj[7]>1:
						return 'True'
					else: return 'True'
				elif obj[0]<=1:
					return 'True'
				else: return 'True'
			elif obj[6]>3:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[13]>3.0:
		return 'True'
	else: return 'True'
