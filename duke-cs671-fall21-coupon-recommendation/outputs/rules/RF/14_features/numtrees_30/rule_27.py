def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[7]>2:
		# {"feature": "Gender", "instances": 30, "metric_value": 0.971, "depth": 2}
		if obj[3]>0:
			# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.9887, "depth": 3}
			if obj[10]<=1.0:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[2]>2:
					# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[5]>0:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]>0:
							return 'True'
						elif obj[6]<=0:
							return 'False'
						else: return 'False'
					elif obj[5]<=0:
						return 'False'
					else: return 'False'
				elif obj[2]<=2:
					return 'False'
				else: return 'False'
			elif obj[10]>1.0:
				# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[13]<=2:
						return 'True'
					elif obj[13]>2:
						return 'False'
					else: return 'False'
				elif obj[6]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]<=0:
			# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[11]>0.0:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[11]<=0.0:
				# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=0:
					return 'False'
				elif obj[5]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[7]<=2:
		return 'True'
	else: return 'True'
