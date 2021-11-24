def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[7]<=11:
		# {"feature": "Time", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Age", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[4]>0:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[5]<=0:
						return 'False'
					elif obj[5]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=0:
				return 'False'
			else: return 'False'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	elif obj[7]>11:
		return 'False'
	else: return 'False'
