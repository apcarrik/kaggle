def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[4]>0:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[7]<=11:
			# {"feature": "Gender", "instances": 17, "metric_value": 0.6723, "depth": 3}
			if obj[3]>0:
				# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[6]>0:
							return 'False'
						elif obj[6]<=0:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		elif obj[7]>11:
			return 'False'
		else: return 'False'
	elif obj[4]<=0:
		return 'False'
	else: return 'False'
