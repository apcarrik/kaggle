def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.8315, "depth": 2}
		if obj[7]>5:
			# {"feature": "Education", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[10]>1.0:
					# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[3]>0:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=2:
							return 'True'
						elif obj[4]>2:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[10]<=1.0:
					return 'True'
				else: return 'True'
			elif obj[6]>2:
				return 'False'
			else: return 'False'
		elif obj[7]<=5:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		return 'False'
	else: return 'False'
