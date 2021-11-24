def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[10]>-1.0:
		# {"feature": "Bar", "instances": 21, "metric_value": 0.9984, "depth": 2}
		if obj[8]>0.0:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[7]>2:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[12]<=2:
					return 'True'
				elif obj[12]>2:
					# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[2]>0:
						# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]<=0:
							return 'False'
						elif obj[3]>0:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]<=2:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]>2:
					return 'False'
				elif obj[2]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[8]<=0.0:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[6]>0:
					# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[5]>0:
						return 'False'
					elif obj[5]<=0:
						return 'True'
					else: return 'True'
				elif obj[6]<=0:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[10]<=-1.0:
		return 'True'
	else: return 'True'
