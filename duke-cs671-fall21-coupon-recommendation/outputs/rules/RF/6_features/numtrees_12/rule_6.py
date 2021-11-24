def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 61, "metric_value": 0.9288, "depth": 2}
		if obj[3]>4:
			# {"feature": "Education", "instances": 37, "metric_value": 0.9995, "depth": 3}
			if obj[2]>0:
				# {"feature": "Passanger", "instances": 26, "metric_value": 0.9612, "depth": 4}
				if obj[0]>0:
					# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Distance", "instances": 21, "metric_value": 0.9984, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					elif obj[4]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[2]<=0:
				# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[5]<=1:
							return 'True'
						elif obj[5]>1:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[4]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]<=4:
			# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.5436, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Education", "instances": 17, "metric_value": 0.6723, "depth": 4}
				if obj[2]<=1:
					# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[0]>1:
						# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				elif obj[2]>1:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[0]>0:
						# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=1:
							return 'True'
						elif obj[5]>1:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]>1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]>3:
		# {"feature": "Occupation", "instances": 24, "metric_value": 0.9183, "depth": 2}
		if obj[3]<=12:
			# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.971, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Passanger", "instances": 16, "metric_value": 1.0, "depth": 4}
				if obj[0]>0:
					# {"feature": "Distance", "instances": 15, "metric_value": 0.9968, "depth": 5}
					if obj[5]>1:
						# {"feature": "Education", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[2]>1:
							return 'True'
						elif obj[2]<=1:
							return 'True'
						else: return 'True'
					elif obj[5]<=1:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[3]>12:
			return 'False'
		else: return 'False'
	else: return 'False'
