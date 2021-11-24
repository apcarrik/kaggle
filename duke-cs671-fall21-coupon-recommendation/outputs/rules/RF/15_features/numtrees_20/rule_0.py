def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Age", "instances": 34, "metric_value": 0.9082, "depth": 2}
		if obj[5]<=4:
			# {"feature": "Occupation", "instances": 28, "metric_value": 0.9666, "depth": 3}
			if obj[8]<=16:
				# {"feature": "Coffeehouse", "instances": 24, "metric_value": 0.8709, "depth": 4}
				if obj[11]<=3.0:
					# {"feature": "Distance", "instances": 21, "metric_value": 0.7025, "depth": 5}
					if obj[14]>1:
						# {"feature": "Time", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[1]>0:
							# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[7]>0:
								# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[0]>1:
									# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[9]>2:
										# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3]<=0:
											return 'False'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[9]<=2:
										return 'False'
									else: return 'False'
								elif obj[0]<=1:
									# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=2:
											return 'True'
										elif obj[9]>2:
											return 'False'
										else: return 'False'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]<=0:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[14]<=1:
						return 'True'
					else: return 'True'
				elif obj[11]>3.0:
					return 'False'
				else: return 'False'
			elif obj[8]>16:
				return 'False'
			else: return 'False'
		elif obj[5]>4:
			return 'True'
		else: return 'True'
	elif obj[2]>3:
		# {"feature": "Bar", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[10]<=2.0:
			# {"feature": "Age", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[5]<=6:
				return 'False'
			elif obj[5]>6:
				return 'True'
			else: return 'True'
		elif obj[10]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'
