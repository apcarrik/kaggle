def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Maritalstatus", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[7]>0:
		# {"feature": "Coupon", "instances": 27, "metric_value": 0.9751, "depth": 2}
		if obj[3]<=3:
			# {"feature": "Weather", "instances": 19, "metric_value": 0.9819, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Occupation", "instances": 17, "metric_value": 0.9367, "depth": 4}
				if obj[10]>4:
					# {"feature": "Age", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[6]>0:
						# {"feature": "Time", "instances": 12, "metric_value": 1.0, "depth": 6}
						if obj[2]<=1:
							# {"feature": "Income", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[11]>4:
								# {"feature": "Coffeehouse", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[13]<=1.0:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[14]<=1.0:
										return 'True'
									elif obj[14]>1.0:
										# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4]<=0:
											return 'False'
										elif obj[4]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[13]>1.0:
									return 'False'
								else: return 'False'
							elif obj[11]<=4:
								return 'True'
							else: return 'True'
						elif obj[2]>1:
							# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[12]<=2.0:
								return 'False'
							elif obj[12]>2.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]<=0:
						return 'True'
					else: return 'True'
				elif obj[10]<=4:
					return 'True'
				else: return 'True'
			elif obj[1]>1:
				return 'False'
			else: return 'False'
		elif obj[3]>3:
			return 'False'
		else: return 'False'
	elif obj[7]<=0:
		return 'True'
	else: return 'True'
