def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[2]>1:
		# {"feature": "Passanger", "instances": 24, "metric_value": 0.8113, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Age", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[4]<=6:
				# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[5]>1:
					# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[6]>6:
						# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[8]>1.0:
							return 'True'
						elif obj[8]<=1.0:
							return 'False'
						else: return 'False'
					elif obj[6]<=6:
						return 'False'
					else: return 'False'
				elif obj[5]<=1:
					return 'True'
				else: return 'True'
			elif obj[4]>6:
				return 'False'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Time", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=0:
					return 'False'
				elif obj[3]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 2}
		if obj[6]>5:
			return 'False'
		elif obj[6]<=5:
			return 'True'
		else: return 'True'
	else: return 'False'
