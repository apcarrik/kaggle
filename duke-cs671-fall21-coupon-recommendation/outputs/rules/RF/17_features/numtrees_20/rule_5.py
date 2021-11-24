def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[9]<=2:
		# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.868, "depth": 2}
		if obj[14]>0.0:
			# {"feature": "Time", "instances": 36, "metric_value": 0.8113, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Age", "instances": 29, "metric_value": 0.6632, "depth": 4}
				if obj[6]>1:
					# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.2975, "depth": 5}
					if obj[13]<=2.0:
						return 'True'
					elif obj[13]>2.0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[6]<=1:
					# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[10]<=12:
						# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[3]>0:
							# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[7]<=0:
								return 'True'
							elif obj[7]>0:
								return 'False'
							else: return 'False'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					elif obj[10]>12:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]>2:
				# {"feature": "Children", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[8]<=0:
					# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						return 'False'
					else: return 'False'
				elif obj[8]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[14]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[9]>2:
		# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[10]<=12:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[3]>0:
					# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]<=1:
						# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[11]<=4:
							return 'False'
						elif obj[11]>4:
							return 'True'
						else: return 'True'
					elif obj[2]>1:
						return 'True'
					else: return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		elif obj[10]>12:
			return 'False'
		else: return 'False'
	else: return 'False'
