def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[4]<=4:
		# {"feature": "Direction_same", "instances": 16, "metric_value": 0.9887, "depth": 2}
		if obj[10]<=0:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[6]>4:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[11]>1:
					# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[2]>1:
						return 'True'
					elif obj[2]<=1:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[11]<=1:
					return 'False'
				else: return 'False'
			elif obj[6]<=4:
				return 'False'
			else: return 'False'
		elif obj[10]>0:
			return 'True'
		else: return 'True'
	elif obj[4]>4:
		return 'True'
	else: return 'True'
