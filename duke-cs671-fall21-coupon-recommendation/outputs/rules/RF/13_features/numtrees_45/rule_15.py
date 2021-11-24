def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[9]>0.0:
		# {"feature": "Time", "instances": 18, "metric_value": 1.0, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[4]<=5:
					return 'False'
				elif obj[4]>5:
					# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>0:
						return 'True'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]>1:
				# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[7]<=12:
					return 'True'
				elif obj[7]>12:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[9]<=0.0:
		return 'False'
	else: return 'False'
