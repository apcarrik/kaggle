def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Maritalstatus", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[7]<=2:
		# {"feature": "Coupon", "instances": 47, "metric_value": 0.9252, "depth": 2}
		if obj[3]>1:
			# {"feature": "Income", "instances": 37, "metric_value": 0.8004, "depth": 3}
			if obj[11]<=3:
				# {"feature": "Bar", "instances": 20, "metric_value": 0.971, "depth": 4}
				if obj[12]<=2.0:
					# {"feature": "Time", "instances": 16, "metric_value": 1.0, "depth": 5}
					if obj[2]>0:
						# {"feature": "Education", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[9]>0:
							# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[10]<=8:
								# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Coupon_validity", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[4]>0:
										# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[1]<=0:
											return 'True'
										elif obj[1]>0:
											return 'False'
										else: return 'False'
									elif obj[4]<=0:
										return 'False'
									else: return 'False'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							elif obj[10]>8:
								return 'False'
							else: return 'False'
						elif obj[9]<=0:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[12]>2.0:
					return 'True'
				else: return 'True'
			elif obj[11]>3:
				# {"feature": "Age", "instances": 17, "metric_value": 0.3228, "depth": 4}
				if obj[6]<=4:
					return 'True'
				elif obj[6]>4:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[3]<=1:
			# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[16]<=2:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[16]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[7]>2:
		return 'False'
	else: return 'False'
