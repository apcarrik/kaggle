def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[2]>1:
		# {"feature": "Distance", "instances": 30, "metric_value": 0.9183, "depth": 2}
		if obj[14]<=2:
			# {"feature": "Income", "instances": 25, "metric_value": 0.971, "depth": 3}
			if obj[9]>0:
				# {"feature": "Gender", "instances": 20, "metric_value": 0.8813, "depth": 4}
				if obj[4]>0:
					# {"feature": "Coupon_validity", "instances": 12, "metric_value": 1.0, "depth": 5}
					if obj[3]<=0:
						# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					elif obj[3]>0:
						# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[1]>0:
							return 'False'
						elif obj[1]<=0:
							# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			elif obj[9]<=0:
				# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[14]>2:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		return 'False'
	else: return 'False'
