def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[2]>0:
		# {"feature": "Age", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Occupation", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[5]>5:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]>0:
							return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				elif obj[5]<=5:
					return 'False'
				else: return 'False'
			elif obj[4]>2:
				return 'True'
			else: return 'True'
		elif obj[3]>2:
			# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[9]<=0:
				return 'False'
			elif obj[9]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
