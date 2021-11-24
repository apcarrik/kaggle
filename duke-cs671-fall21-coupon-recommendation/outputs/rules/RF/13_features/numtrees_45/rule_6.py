def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.971, "depth": 2}
		if obj[9]<=2.0:
			# {"feature": "Time", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[7]<=6:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]<=3:
						return 'True'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				elif obj[7]>6:
					return 'False'
				else: return 'False'
			elif obj[1]>1:
				return 'False'
			else: return 'False'
		elif obj[9]>2.0:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
