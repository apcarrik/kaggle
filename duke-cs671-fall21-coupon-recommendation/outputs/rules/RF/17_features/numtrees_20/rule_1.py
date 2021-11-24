def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Time", "instances": 51, "metric_value": 0.8974, "depth": 1}
	if obj[2]<=1:
		# {"feature": "Distance", "instances": 26, "metric_value": 0.9957, "depth": 2}
		if obj[16]>1:
			# {"feature": "Bar", "instances": 17, "metric_value": 0.9774, "depth": 3}
			if obj[12]<=2.0:
				# {"feature": "Passanger", "instances": 14, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Age", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[6]<=4:
						# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[9]<=3:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[14]<=2.0:
									return 'False'
								elif obj[14]>2.0:
									return 'True'
								else: return 'True'
							elif obj[9]>3:
								return 'True'
							else: return 'True'
						elif obj[3]>2:
							return 'True'
						else: return 'True'
					elif obj[6]>4:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[12]>2.0:
				return 'False'
			else: return 'False'
		elif obj[16]<=1:
			# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[12]>0.0:
				return 'True'
			elif obj[12]<=0.0:
				# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[6]<=1:
					return 'True'
				elif obj[6]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[2]>1:
		# {"feature": "Education", "instances": 25, "metric_value": 0.6343, "depth": 2}
		if obj[9]>1:
			# {"feature": "Bar", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[12]>0.0:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[10]<=21:
					return 'True'
				elif obj[10]>21:
					return 'False'
				else: return 'False'
			elif obj[12]<=0.0:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[9]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'
