def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Age", "instances": 24, "metric_value": 0.995, "depth": 2}
		if obj[4]>1:
			# {"feature": "Time", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[6]>0:
					# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]>4:
						return 'True'
					elif obj[7]<=4:
						return 'False'
					else: return 'False'
				elif obj[6]<=0:
					return 'False'
				else: return 'False'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		elif obj[4]<=1:
			# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[9]<=1.0:
				return 'False'
			elif obj[9]>1.0:
				# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]<=3:
						return 'False'
					elif obj[6]>3:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
