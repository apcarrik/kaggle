def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[14]<=1:
		# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.7642, "depth": 2}
		if obj[11]>0.0:
			# {"feature": "Passanger", "instances": 14, "metric_value": 0.3712, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[11]<=0.0:
			# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[5]>0:
				return 'False'
			elif obj[5]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[14]>1:
		# {"feature": "Time", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[1]>1:
			# {"feature": "Income", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[9]<=4:
				# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[3]>0:
					# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[2]>2:
						return 'False'
					elif obj[2]<=2:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>1:
							# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[8]>4:
								return 'False'
							elif obj[8]<=4:
								return 'True'
							else: return 'True'
						elif obj[0]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[9]>4:
				return 'False'
			else: return 'False'
		elif obj[1]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
