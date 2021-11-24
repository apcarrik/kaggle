def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[3]>0:
		# {"feature": "Time", "instances": 27, "metric_value": 0.951, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Income", "instances": 24, "metric_value": 0.9799, "depth": 3}
			if obj[10]<=4:
				# {"feature": "Weather", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Children", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[7]>0:
						return 'True'
					elif obj[7]<=0:
						# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[5]>0:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]>0:
								return 'False'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						elif obj[5]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			elif obj[10]>4:
				# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=0:
					# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[8]>0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[8]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]>3:
			return 'True'
		else: return 'True'
	elif obj[3]<=0:
		# {"feature": "Weather", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[1]<=1:
			return 'False'
		elif obj[1]>1:
			return 'True'
		else: return 'True'
	else: return 'False'
