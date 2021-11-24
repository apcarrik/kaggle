def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Restaurant20to50", "instances": 40, "metric_value": 1.0, "depth": 2}
		if obj[14]>0.0:
			# {"feature": "Occupation", "instances": 32, "metric_value": 0.9745, "depth": 3}
			if obj[10]>6:
				# {"feature": "Maritalstatus", "instances": 17, "metric_value": 0.7871, "depth": 4}
				if obj[7]<=2:
					# {"feature": "Income", "instances": 14, "metric_value": 0.5917, "depth": 5}
					if obj[11]<=6:
						# {"feature": "Weather", "instances": 13, "metric_value": 0.3912, "depth": 6}
						if obj[1]<=0:
							return 'False'
						elif obj[1]>0:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>0:
								return 'False'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[11]>6:
						return 'True'
					else: return 'True'
				elif obj[7]>2:
					# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[10]<=6:
				# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[9]>0:
					# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[3]>0:
						# {"feature": "Time", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]>0:
								return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[9]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[14]<=0.0:
			# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[7]<=1:
				return 'True'
			elif obj[7]>1:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Time", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[2]>0:
			return 'True'
		elif obj[2]<=0:
			# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[6]<=4:
				return 'True'
			elif obj[6]>4:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
