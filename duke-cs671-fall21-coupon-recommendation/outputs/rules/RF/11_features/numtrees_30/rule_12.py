def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.7871, "depth": 1}
	if obj[3]>1:
		# {"feature": "Education", "instances": 25, "metric_value": 0.9044, "depth": 2}
		if obj[4]>0:
			# {"feature": "Bar", "instances": 17, "metric_value": 0.9975, "depth": 3}
			if obj[6]<=1.0:
				# {"feature": "Distance", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[10]>1:
					# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[5]<=9:
							return 'True'
						elif obj[5]>9:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[10]<=1:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[5]>11:
						return 'False'
					elif obj[5]<=11:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[6]>1.0:
				return 'False'
			else: return 'False'
		elif obj[4]<=0:
			return 'True'
		else: return 'True'
	elif obj[3]<=1:
		return 'True'
	else: return 'True'
