def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[7]<=12:
		# {"feature": "Distance", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[13]>1:
			# {"feature": "Passanger", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Age", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[4]>1:
					# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[1]>1:
						# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[10]>0.0:
							return 'True'
						elif obj[10]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[13]<=1:
			return 'True'
		else: return 'True'
	elif obj[7]>12:
		return 'False'
	else: return 'False'
