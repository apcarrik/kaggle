def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[7]<=2:
		# {"feature": "Passanger", "instances": 42, "metric_value": 0.9587, "depth": 2}
		if obj[0]>1:
			# {"feature": "Bar", "instances": 21, "metric_value": 0.7025, "depth": 3}
			if obj[10]<=0.0:
				# {"feature": "Age", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=6:
					# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[8]<=7:
						# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]>0:
								return 'True'
							elif obj[6]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[8]>7:
						return 'False'
					else: return 'False'
				elif obj[5]>6:
					return 'False'
				else: return 'False'
			elif obj[10]>0.0:
				return 'True'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[8]<=10:
				# {"feature": "Distance", "instances": 14, "metric_value": 0.9852, "depth": 4}
				if obj[14]<=2:
					# {"feature": "Coupon", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[2]>2:
						# {"feature": "Age", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[5]>0:
							# {"feature": "Income", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[9]>2:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[12]<=0.0:
									# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[1]>1:
										return 'True'
									else: return 'True'
								elif obj[12]>0.0:
									return 'False'
								else: return 'False'
							elif obj[9]<=2:
								return 'True'
							else: return 'True'
						elif obj[5]<=0:
							return 'False'
						else: return 'False'
					elif obj[2]<=2:
						return 'True'
					else: return 'True'
				elif obj[14]>2:
					return 'False'
				else: return 'False'
			elif obj[8]>10:
				# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[7]>2:
		# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[14]<=2:
			return 'False'
		elif obj[14]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
