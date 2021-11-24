def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[6]<=10:
			# {"feature": "Age", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[4]>1:
				return 'False'
			elif obj[4]<=1:
				# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[8]>0.0:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]>0:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]>2:
							return 'False'
						elif obj[2]<=2:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[8]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[6]>10:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[2]>1:
				return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.3712, "depth": 2}
		if obj[6]<=12:
			return 'True'
		elif obj[6]>12:
			return 'False'
		else: return 'False'
	else: return 'True'
