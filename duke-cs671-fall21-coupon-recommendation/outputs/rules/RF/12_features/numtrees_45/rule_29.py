def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Distance", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[11]<=2:
			# {"feature": "Age", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[4]<=4:
				# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[7]>0.0:
					# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[1]<=0:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=1:
							return 'True'
						elif obj[6]>1:
							return 'False'
						else: return 'False'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				elif obj[7]<=0.0:
					# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[3]>0:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]>1:
							return 'True'
						elif obj[6]<=1:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]>4:
				return 'False'
			else: return 'False'
		elif obj[11]>2:
			return 'False'
		else: return 'False'
	elif obj[2]>3:
		return 'False'
	else: return 'False'
