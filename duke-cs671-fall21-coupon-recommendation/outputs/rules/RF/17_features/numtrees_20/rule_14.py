def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[13]>0.0:
		# {"feature": "Income", "instances": 39, "metric_value": 0.9995, "depth": 2}
		if obj[11]>0:
			# {"feature": "Maritalstatus", "instances": 35, "metric_value": 0.9947, "depth": 3}
			if obj[7]>0:
				# {"feature": "Occupation", "instances": 27, "metric_value": 0.9911, "depth": 4}
				if obj[10]<=16:
					# {"feature": "Distance", "instances": 22, "metric_value": 0.9457, "depth": 5}
					if obj[16]>1:
						# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[14]>0.0:
							return 'True'
						elif obj[14]<=0.0:
							# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[4]>0:
								return 'False'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[16]<=1:
						# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Children", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[8]<=0:
								# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[6]<=1:
									# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[9]>1:
										return 'True'
									elif obj[9]<=1:
										return 'False'
									else: return 'False'
								elif obj[6]>1:
									return 'False'
								else: return 'False'
							elif obj[8]>0:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[10]>16:
					# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]<=3:
						return 'False'
					elif obj[2]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]<=0:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[16]>1:
					return 'False'
				elif obj[16]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[11]<=0:
			return 'True'
		else: return 'True'
	elif obj[13]<=0.0:
		# {"feature": "Maritalstatus", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[7]<=2:
			return 'False'
		elif obj[7]>2:
			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
