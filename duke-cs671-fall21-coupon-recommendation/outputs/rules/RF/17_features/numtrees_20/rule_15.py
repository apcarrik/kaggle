def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Income", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[11]<=7:
		# {"feature": "Time", "instances": 46, "metric_value": 0.9877, "depth": 2}
		if obj[2]>0:
			# {"feature": "Occupation", "instances": 35, "metric_value": 0.9947, "depth": 3}
			if obj[10]>4:
				# {"feature": "Coupon_validity", "instances": 28, "metric_value": 0.9403, "depth": 4}
				if obj[4]<=0:
					# {"feature": "Coupon", "instances": 16, "metric_value": 0.6962, "depth": 5}
					if obj[3]>2:
						return 'True'
					elif obj[3]<=2:
						# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]>0:
					# {"feature": "Weather", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[1]<=0:
						# {"feature": "Maritalstatus", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[7]>0:
							# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[9]>0:
								return 'False'
							elif obj[9]<=0:
								# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]>2:
									return 'True'
								elif obj[3]<=2:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[7]<=0:
							return 'True'
						else: return 'True'
					elif obj[1]>0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[10]<=4:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=0:
			# {"feature": "Age", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[6]<=5:
				return 'False'
			elif obj[6]>5:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[11]>7:
		return 'True'
	else: return 'True'
