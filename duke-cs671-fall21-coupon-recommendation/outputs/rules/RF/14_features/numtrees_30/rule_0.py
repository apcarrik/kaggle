def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[13]<=2:
		# {"feature": "Coupon", "instances": 31, "metric_value": 0.9383, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Time", "instances": 22, "metric_value": 0.7732, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Occupation", "instances": 14, "metric_value": 0.3712, "depth": 4}
				if obj[7]<=18:
					return 'True'
				elif obj[7]>18:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[10]>0.0:
						return 'True'
					elif obj[10]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[6]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]>3:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[4]>1:
					return 'False'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			elif obj[6]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[13]>2:
		return 'False'
	else: return 'False'
