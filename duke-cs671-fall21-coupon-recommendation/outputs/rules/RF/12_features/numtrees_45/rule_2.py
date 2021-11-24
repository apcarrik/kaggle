def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[6]<=7:
		# {"feature": "Education", "instances": 14, "metric_value": 0.9852, "depth": 2}
		if obj[5]>0:
			# {"feature": "Passanger", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[0]<=2:
				return 'True'
			elif obj[0]>2:
				# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[8]<=1.0:
					return 'False'
				elif obj[8]>1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]<=0:
			return 'False'
		else: return 'False'
	elif obj[6]>7:
		return 'False'
	else: return 'False'
